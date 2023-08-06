"""Define functions for scaling and cropping images"""

import shlex
import tempfile
from pathlib import Path
from subprocess import check_call

from chameleon import PageTemplate
from PIL import Image as PILImage


def crop_image(input_image_path, output_image_path, area=(0, 0, 0, 0)):
    """Crop :input_image_path: and save to :output_image_path
    :area: is a tuple of 4 coordinates
    """
    img = PILImage.open(input_image_path)
    cropped_img = img.crop(area)
    cropped_img.save(output_image_path)


def scale_image(input_image_path, output_image_path, width=None, height=None):
    """Scale an image and keep the aspect ratio.
    :input_image_path: origin al image
    :output_image_path: path to write the scaled image
    :width: new width
    :height: new height"""
    original_image = PILImage.open(input_image_path)
    w, h = original_image.size
    (
        "The original image size is {wide} wide x {height} "
        "high".format(wide=w, height=h)
    )

    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError("Width or height required!")

    original_image.thumbnail(max_size, PILImage.ANTIALIAS)
    original_image.save(output_image_path)

    scaled_image = PILImage.open(output_image_path)
    width, height = scaled_image.size
    (
        "The scaled image size is {wide} wide x {height} "
        "high".format(wide=width, height=height)
    )


PHANTOM_JS_CODE_TEMPLATE = PageTemplate(
    """
<script tal:omit-tag tal:define="filename filename" tal:define="url url">
var page = require('webpage').create();
page.open('${url}', function() {
  page.render('${filename}');
  phantom.exit();
});
</script>
"""
)


def get_scaled_screenshot(
    url,
    v_crop=305,
    scale_factor=1.3,
    phantomjs_bin="/usr/local/bin/phantomjs",
    code_template=None,
):
    code_template = PHANTOM_JS_CODE_TEMPLATE if code_template is None else code_template
    png_suffix = ".png"
    code = code_template.render(
        filename=(input_image_path := tempfile.mkstemp(suffix=png_suffix)[1]), url=url,
    )
    (code_file,) = (Path(fp) for _, fp in (tempfile.mkstemp(suffix=".js"),))
    code_file.write_text(code)
    check_call(shlex.split(f"{phantomjs_bin} {code_file}"))

    with PILImage.open(input_image_path) as img:
        w, h = img.size
    area = (0, v_crop, w, v_crop * 2)

    crop_image(
        input_image_path,
        output_image_path := tempfile.mkstemp(suffix=png_suffix)[1],
        area=area,
    )
    with PILImage.open(output_image_path) as img:
        w, h = img.size
    scale_image(
        output_image_path,
        scale_image_path := tempfile.mkstemp(suffix=png_suffix)[1],
        width=w // scale_factor,
        height=None,
    )
    return scale_image_path
