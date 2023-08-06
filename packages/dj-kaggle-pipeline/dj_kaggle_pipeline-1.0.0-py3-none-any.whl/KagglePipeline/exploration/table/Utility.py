class Timing:
    """
    Utility class to time the notebook while running. 
    """
    def __init__(self, start_time):
        self.start_time = start_time
        self.counter = 0

    def timer(self, message=None):
        """
        Timing function that returns the time taken for this step since the starting time. Message is optional otherwise we use a counter. 
        """
        if message:
            print(f"{message} at {time.time()-self.start_time}")
        else:
            print(f"{self.counter} at {time.time()-self.start_time}")
            self.counter += 1
        return


def guess_types(data, top_count=4, threshold=0.5):
    """
    Attempts to estimate the nature of the datatypes in a pandas DataFrame, 
    If the data can be cast to a number without error we assume it is numerical
    If the top (top_count) "strings" or text values in the column occur for more than threshold % of the column we call it a category
    Otherwise its a string


    Returns numericals, strings, categoricals, date where 
        numericals is a list of columns that have a numerical data type
        strings is a list of columns that have a text data type
        categoricals is a list of columns that are categorical type
        date is a list of columns that are DateTime type


    """
    numericals = []
    categoricals = []
    strings = []
    dates = []
    for col in data:
        try:
            data[col].astype("float64")
            numericals.append(col)
        except:
            try:
                data[col].astype("datetime64")
                dates.append(col)
            except:
                value = sum(data[col].value_counts()[0:top_count])
                if value/len(data[col]) >= threshold:
                    categoricals.append(col)
                else:
                    strings.append(col)
    return numericals, strings, categoricals, dates

