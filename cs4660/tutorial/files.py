import lists
"""Files tests simple file read related operations"""

class SimpleFile(object):
    """SimpleFile tests using file read api to do some simple math"""
    def __init__(self, file_path):
        self.numbers = []
        """
        TODO: reads the file by path and parse content into two
        dimension array (numbers)
        """
        with open(file_path) as f:
            for line in f:
                self.numbers.append([int(x) for x in line.split()])

    def get_mean(self, line_number):
        return lists.get_avg(self.numbers[line_number])
        """
        get_mean retrieves the mean value of the list by line_number (starts
        with zero)
        """
        pass

    def get_max(self, line_number):
        return max(self.numbers[line_number])
        """
        get_max retrieves the maximum value of the list by line_number (starts
        with zero)
        """
        pass

    def get_min(self, line_number):
        return min(self.numbers[line_number])
        """
        get_min retrieves the minimum value of the list by line_number (starts
        with zero)
        """
        pass

    def get_sum(self, line_number):
        return lists.get_sum(self.numbers[line_number])
        """
        get_sum retrieves the sumation of the list by line_number (starts with
        zero)
        """
        pass
