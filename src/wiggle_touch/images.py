from dataclasses import dataclass
import os
from pathlib import Path
from functools import cached_property

BASE_FOLDER = Path.home() / "WiggleR"
IMG_FOLDER = BASE_FOLDER / "Pictures"


@dataclass(frozen=True)
class Images:
    folder: Path = BASE_FOLDER / IMG_FOLDER

    def __getitem__(self, index: int):
        return self.folder / self.images[index]

    @cached_property
    def images(self):
        return sorted(os.listdir(self.folder))

    @cached_property
    def count(self) -> int:
        return len(self.images) - 1

    @cached_property
    def last(self) -> str:
        return self.folder / self.images[self.count]
