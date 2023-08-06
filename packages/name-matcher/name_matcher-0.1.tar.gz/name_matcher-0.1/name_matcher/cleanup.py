import itertools

class CleanUp:
    def __init__(self):
        self.match_percentage = ''
        self.match_count = ''
        self.saved_outcome = ''
        self.saved_match_count = ''
        self.saved_combined_length = ''
        self.combined_lenth = ''
        
    def normalize_string(self, name):
        """
        This method replaces common mistakes with letters to make it uniform and phonetically flat
        """
        name = str(name).upper()
        name = name.replace('@', 'A')
        name = name.replace('$', 'S')
        name = name.replace('0', 'O')
        name = name.replace('5', 'S')
        name = name.replace('1', 'I')
        name = name.replace('6', 'B')
        name = name.replace('Z', 'S')
        name = name.replace('OH', 'O')
        name = name.replace('CH', 'SH')
        name = name.replace('PH', 'F')
        name = name.replace('C', 'K')
        name = name.replace('J', 'G')
        name = name.replace('EI', 'IE')
        name = name.replace('AE', 'EA')
        name = name.replace('ER', 'AR')
        if name[-1] == 'E':
            name = name[:-1]
        if name[-1] == 'H':
            name = name[:-1]
        return name
        
    def keep_alphabets(self, name):
        """
        This method removes all non alphabet characters from the string
        """
        name = ''.join([i for i in str(name).strip() if i.isalpha()])
        return name
    
    def remove_adjacent_duplicates(self, name):
        """
        This method replaces repeating characters with only one of such character
        """
        name = ''.join(i for i, _ in itertools.groupby(name))
        return name
    
    def name_cleanup(self, name):
        """
        This method calls other 3 methods to perform cleanup
        args: name
        return: cleaned up name
        """
        name = self.normalize_string(name)
        name = self.keep_alphabets(name)
        name = self.remove_adjacent_duplicates(name)
        return name