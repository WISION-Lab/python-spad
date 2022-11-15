import json
from pathlib import Path
from scipy.io import loadmat


class SPADLoader:
    def __init__(self, dirname):
        self.dirname = dirname
        with open(Path(dirname, "info.json"), "r") as info_file:
            json_data = json.load(info_file)
            self.n_parts = json_data["no_parts"]
            self.frames_per_part = json_data["no_frames"]
            self.n_frames = self.n_parts * self.frames_per_part
        self.frame_index = 0
        self.part_array = None

    def __iter__(self):
        return self

    def __len__(self):
        return self.n_frames

    def __next__(self):
        if self.frame_index >= self.n_frames:
            raise StopIteration()
        part_offset = self.frame_index % self.frames_per_part
        if part_offset == 0:
            # If this frame is the first in its part then we need to
            # load a new part file.
            part_index = self.frame_index // self.frames_per_part
            part_pathname = Path(self.dirname, f"part_{part_index + 1}.mat")
            self.part_array = loadmat(str(part_pathname))["OUTPUT"]
        self.frame_index += 1
        return self.part_array[..., part_offset]
