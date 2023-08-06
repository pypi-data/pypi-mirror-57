from .dataset import Dataset


class Images(Dataset):
    @staticmethod
    def get_type():
        return 'images'
