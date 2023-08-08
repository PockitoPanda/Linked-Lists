class Node:
    """ For use in a Linked List"""
    def __init__(self, data, next=None):
        self._data = data
        self._next = next


class Contact:
    """ A simple class to contain the name and phone number of a contact in a phone book """
    def __init__(self, name, number):
        self._name = name
        self._number = number


class ContactList:
    """ A class """
    def __init__(self):
        """ self._head is the head pointer to a linked list of Nodes. Starts off empty"""
        self._head = None

    def add(self, contact_name, contact_number):
        # 1. Create a new Contact object with the incoming parameters
        new_contact = Contact(contact_name, contact_number)
        # 2. Create a new Node object with the new Contact as its data
        new_node = Node(new_contact)
        # 3. Find the correct location for the Node in the list referenced by self._head
        #           1. Linked List is empty
        if self._head is None:
            self._head = new_node
            return
        #           2. Linked List is not empty but the new Node goes at the front
        probe = self._head
        previous = None
        while probe is not None:
            if contact_name < probe._data._name:
                new_node._next = probe
                self._head = new_node
                if previous is not None:
                    previous._next = new_node
                return
            elif contact_name > probe._data._name and probe._next is None:
                probe._next = new_node
                return
            else:
                previous = probe
                probe = probe._next
        #           3. Linked List is not empty and the new Node goes in the middle
        #           4. Linked List is not empty and the new Node goes at the end

    def remove(self, contact_name):
        probe = self._head
        previous = None
        while probe is not None:
            if probe._data._name == contact_name:
                if probe._next is None and previous is None:
                    self._head = None
                elif probe._next is None and previous is not None:
                    previous._next = None
                elif previous is not None and probe._next is not None:
                    previous._next = probe._next
                elif previous is None and probe._next is not None:
                    self._head = probe._next
            previous = probe
            probe = probe._next
            
    def change_phone_number(self, name, new_number):
        probe = self._head
        while probe is not None:
            if probe._data._name == name:
                probe._data._number = new_number
                return
            else:
                probe = probe._next
        print("There is no name that matches your entry, please try again.")
    
    def __str__(self):
        str_print = ""
        probe = self._head
        while probe is not None:
            str_print += f"Name: {probe._data._name} Number: {probe._data._number}\n"
            probe = probe._next
        return str_print