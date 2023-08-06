import tempfile
from pathlib import Path

import pytest
from PIL import Image
from PIL import ImageDraw

from chamelboots.imageutils import crop_image
from chamelboots.imageutils import get_scaled_screenshot
from chamelboots.imageutils import scale_image


def test_scale_image():
    """Test image scaling. Forgot to use builtin tmpfile in Pytest."""
    size = width, height = (60, 30)
    suffix = ".png"
    img = Image.new("RGB", size, color="red")
    (input_image_path, output_image_path, crop_image_path) = (
        Path(fp) for _, fp in (tempfile.mkstemp(suffix=suffix) for _ in range(3))
    )
    img.save(input_image_path)
    scale_image(input_image_path, output_image_path, width=height)
    with Image.open(output_image_path) as img:
        w, h = img.size
        assert w == height
    crop_image(output_image_path, crop_image_path, area=(0, ll := (h // 2) + 1, w, h))
    with Image.open(crop_image_path) as img:
        assert img.size == (w, ll - 1)  # subtract one because of rounding
    scale_image(input_image_path, output_image_path, height=width)
    with Image.open(output_image_path) as img:
        w, h = img.size
        assert h == height
    scale_image(input_image_path, output_image_path, height=height, width=width)
    with Image.open(output_image_path) as img:
        w, h = img.size
        assert w == width
        assert h == height

    with pytest.raises(RuntimeError):
        scale_image(input_image_path, output_image_path)


def test_scaled_screenshot():
    """docstring for test_scaled_screenshot"""
    image = get_scaled_screenshot("http://example.com")
    with Image.open(image) as fh:
        assert all(item > 0 for item in fh.size)
