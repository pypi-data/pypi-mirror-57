import pickle
from threading import Timer
import copy
import os
from optimeed.core.tools import rgetattr, text_format, indentParagraph, applyEquation
import traceback
from optimeed.core.tools import getPath_workspace
try:
    import pandas as pd
except ModuleNotFoundError:
    print("Failed to import pandas. Excel export might fail.")


class DataSave:
    def __init__(self, filename='', change_filename_if_exists=True):
        if not filename:
            self.filename = getPath_workspace() + '/default_collection'
        else:
            self.filename = os.path.abspath(filename)

        self.theData = None

        self.set_filename(self.filename, change_filename_if_exists)
        self.info = ''
        self.timer = None

    def get_info(self):
        return self.info

    def set_info(self, info):
        self.info = info

    def save(self, safe_save=True):
        if not os.path.exists(os.path.dirname(self.filename)):
            os.makedirs(os.path.dirname(self.filename))

        if os.path.exists(self.filename) and safe_save:
            temp_file = self.filename + 'temp'
            f = open(temp_file, 'wb')
            pickle.dump(self, f)
            f.close()
            os.replace(temp_file, self.filename)
        else:
            f = open(self.filename, 'wb')
            pickle.dump(self, f)
            f.close()

    @staticmethod
    def get_extension():
        return ".datasaved"

    def get_data(self):
        return self.theData

    def set_data(self, theData):
        self.theData = theData

    @staticmethod
    def load(filename, doCoherence=True):
        if filename:
            try:
                from time import time
                if not os.path.splitext(filename)[-1].lower():
                    filename += Collection.get_extension()
                theFile = open(filename, 'rb')
                theCollection = pickle.load(theFile)
                theFile.close()
                theCollection.filename = filename
                if doCoherence:
                    theCollection.coherence()
                return theCollection
            except pickle.UnpicklingError:
                print("Could not unpickle file ! " + filename)
                print(traceback.format_exc())
            except OSError:
                print("Could not read file ! " + filename)
                print(traceback.format_exc())
            except EOFError:
                print("File empty ! " + filename)
                print(traceback.format_exc())
        else:
            print("WARNING INVALID COLLECTION FILENAME: " + filename)
        return None

    def coherence(self):
        item = self.get_data()
        newItem = item.__class__()
        try:
            newItem.assign(item)
        except AttributeError:
            pass
        newData = newItem
        self.set_data(newData)

    def get_filename(self):
        return self.filename

    def set_filename(self, filename, change_filename_if_exists):
        if not filename.endswith(self.get_extension()):
            filename += self.get_extension()

        if change_filename_if_exists:
            curr_index = 1
            head, tail = os.path.split(filename)
            base_name = os.path.splitext(tail)[0]
            while os.path.exists(filename):
                filename = head + '/' + base_name + '_' + str(curr_index) + self.get_extension()
                curr_index += 1
        self.filename = filename

    def stop_autosave(self):
        if self.timer is not None:
            self.timer.cancel()

    def start_autosave(self, timer_autosave):
        self.save()
        if timer_autosave > 0:
            self.timer = Timer(timer_autosave, lambda: self.start_autosave(timer_autosave))
            self.timer.daemon = True
            self.timer.start()

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["timer"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.timer = None

    def __str__(self):
        return self.get_info()


class Collection(DataSave):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theData = []

    @staticmethod
    def get_extension():
        return ".col"

    def add_data(self, data_in):
        self.theData.append(copy.deepcopy(data_in))

    def set_data_at_index(self, data_in, index):
        self.theData[index] = data_in

    def set_attribute_data(self, the_attribute, the_value):
        for item in self.get_data():
            setattr(item, the_attribute, the_value)

    def set_attribute_equation(self, attribute_name, equation_str):
        """
        Advanced method to set the value of attribute_name from equation_str

        :param attribute_name: string (name of the attribute to set)
        :param equation_str: formatted equation, check :meth:`~optimeed.core.CommonFunctions_Library.applyEquation`
        :return:
        """
        for item in self.get_data():
            setattr(item, attribute_name, applyEquation(item, equation_str))

    def get_list_attributes(self, attributeName):
        """
        Get the value of attributeName of all the data in the Collection

        :param attributeName: string (name of the attribute to get)
        :return: list
        """
        if not attributeName:
            return list()
        return [rgetattr(data, attributeName) for data in self.theData]

    def coherence(self):
        """
        Call that method to ensure that all the elements are properly instantiated.
        This method calls the method "assign" from the data structure. If None: skip
        """
        newData = [None] * len(self.get_data())
        for index, item in enumerate(self.get_data()):
            newItem = item.__class__()
            try:
                newItem.assign(item)
            except AttributeError:
                pass
            newData[index] = newItem
        self.theData = newData

    def merge(self, collection):
        """
        Merge a collection with the current collection

        :param collection: :class:`~optimeed.core.Collection.Collection` to merge
        """
        for item in collection.get_data():
            self.add_data(item)

    def delete_points_at_indices(self, indices):
        """
        Delete several elements from the Collection

        :param indices: list of indices to delete
        """
        for index in sorted(indices, reverse=True):
            del self.get_data()[index]

    def export_xls(self, excelFilename, excelsheet='Sheet1', mode='w'):
        """Export the collection to excel. It only exports the direct attributes.

        :param excelFilename: filename of the excel
        :param excelsheet: name of the sheet
        :param mode: 'w' to erase existing file, 'a' to append sheetname to existing file
        """
        if len(self.get_data()):
            attributes = list(vars(self.get_data()[0]).keys())
            dictToExport = dict()
            for attribute in attributes:
                dictToExport[attribute] = [float(rgetattr(data, attribute)) for data in self.theData]

            writer = pd.ExcelWriter(excelFilename)
            if mode == 'a':
                try:
                    alldata = pd.read_excel(excelFilename, sheet_name=None)
                    for key in alldata:
                        alldata[key].to_excel(writer, sheet_name=key, index=False)
                except FileNotFoundError:
                    pass
            df = pd.DataFrame(dictToExport)
            df.to_excel(writer, sheet_name=excelsheet, index=False)
            writer.save()

    def __len__(self):
        return len(self.get_data())
