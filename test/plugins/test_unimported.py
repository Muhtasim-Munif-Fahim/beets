"""Tests for the unimported plugin."""

import pytest

from beets.test.helper import IOMixin, PluginTestHelper

_p = pytest.param


class TestUnimported(IOMixin, PluginTestHelper):
    plugin = "unimported"

    @pytest.mark.parametrize(
        "extension", [_p("mp3", id="simple"), _p("tar.gz", id="compound")]
    )
    def test_ignore_extension(self, extension):
        ignored = self.lib_path / f"archive.{extension}"
        ignored.touch()
        unimported = self.lib_path / "report.txt"
        unimported.touch()
        self.config["unimported"]["ignore_extensions"] = [extension]

        assert self.run_with_output("unimported") == f"{unimported}\n"
