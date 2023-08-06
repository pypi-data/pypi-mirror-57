from .cleanup import CleanUp

class NameMatcher(CleanUp):
    """
    This class doesn't take any arguments
    """
    def __init__(self):
        """
        initialize parent class's init method via super method
        """
        super().__init__()
        
    def initialzie_to_zero(self):
        """
        This method reinitializes all of the instance arguments back to 0 value
        """
        self.match_percentage = 0
        self.match_count = 0
        self.saved_outcome = 0
        self.saved_match_count = 0
        self.saved_combined_length = 0
        self.combined_lenth = 0
        
    def calculate_match_percentage(self, match_count, combined_length):
        """
        This method calculates the percentage of characters matched between the two strings
        args: match_count, combined_length
        return: percentage of characters matched
        """
        percentage = (match_count/combined_length) * 100
        return percentage
    
    def zip_match_names(self, name1, name2):
        """
        This method takes in two names, returns the number of characters matched and total number of characters in both strings
        args: name1, name2
        return: matched_count, combined_length
        """
        self.combined_length = len(name1) + len(name2)
        zipped = zip(name1, name2)
        for i in zipped:
            if i[0]==i[1]:
                self.match_count += 2
        outcome = self.calculate_match_percentage(self.match_count, self.combined_length)
        if outcome < 90 and len(name1)!=len(name2) and outcome>self.saved_outcome:
            self.saved_outcome = outcome
            self.saved_match_count = self.match_count
            self.saved_combined_length = self.combined_length
            self.match_count = 0
            self.combined_length = len(name1) + len(name2)
            zipped = zip(name1, name2)
            remove_one_char = True
            for i, j in enumerate(zipped):
                if j[0]!=j[1] and len(name1)>len(name2) and remove_one_char:
                    name1 = name1[:i]+name1[i+1:]
                    remove_one_char = False
                elif j[0]!=j[1] and len(name1)<len(name2) and remove_one_char:
                    name2 = name2[:i]+name2[i+1:]
                    remove_one_char = False
            self.match_count, self.combined_length = self.zip_match_names(name1, name2)
        elif outcome<self.saved_outcome:
            self.match_count = self.saved_match_count
            self.combined_length = self.saved_combined_length
        return self.match_count, self.combined_length
    
    def name_matcher(self, name1, name2):
        """
        This method takes two names and calls all the methods to perform cleanup, string match and match percentage calculation
        args: name1, name2
        return: match_percentage
        """
        self.initialzie_to_zero()
        name1 = self.name_cleanup(name1)
        name2 = self.name_cleanup(name2)
        self.match_count, self.combined_length = self.zip_match_names(name1, name2)
        self.match_percentage = self.calculate_match_percentage(self.match_count, self.combined_length)
        return self.match_percentage