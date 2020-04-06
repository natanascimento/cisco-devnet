class rename_dict(dict):
    def rename(self, old_key, new_key):
        self[new_key] = self.pop(old_key)