import numpy as np


class PostOffice:
    """A Post Office class. Allows users to message each other.

    Parameters
    ----------
    usernames : list
        Users for which we should create PO Boxes.

    Attributes
    ----------
    message_id : int
        Incremental id of the last message sent.
    is_read : bool
        Indicates whether the message has been read (This is an attribute I added,
        because it is necessary to know if a message has been read or not, for the read_inbox operation).
    boxes : dict
        Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.is_read = False
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_title, message_body, urgent=False):
        """Send a message to a recipient.

        Parameters
        ----------
        sender : str
            The message sender's username.
        recipient : str
            The message recipient's username.
        message_title : str
            The title of the message (This is a parameter I added,
            because the title is necessary for the search_inbox action).
        message_body : str
            The body of the message.
        urgent : bool, optional
            The urgency of the message.
            Urgent messages appear first.

        Returns
        -------
        int
            The message ID, auto incremented number.

        Raises
        ------
               KeyError
                   If the recipient does not exist.

               Examples
               --------
               After creating a PO box and sending a letter,
               the recipient should have 1 message in the
               inbox.

               # >>> po_box = PostOffice(['a', 'b'])
               # >>> message_id = po_box.send_message('a', 'b', 'Hello!')
               # >>> len(po_box.boxes['b'])
               # 1
               # >>> message_id
               1
               """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'title': message_title,
            'body': message_body,
            'sender': sender,
            'isRead': self.is_read,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, num_msg_to_read=0):
        """Read the messages in the inbox.

        Parameters
        ----------
        username : str
            The message recipient's username.
        num_msg_to_read : int, optional
            The number of messages the user wants to read.

        Returns
        -------
        list
            The first N messages in the user's inbox.
        """
        user_box = self.boxes[username]
        if not num_msg_to_read:
            res = [msg for msg in user_box if not msg['isRead']]
        else:
            res = []
            i = 0
            size = len(user_box)
            while num_msg_to_read > 0 and i < size:
                if not user_box[i]['isRead']:
                    res.append(user_box[i])
                    num_msg_to_read -= 1
                i += 1

        for msg in res:
            msg['isRead'] = True
        return res

    def search_inbox(self, username, string):
        """Send a message to a recipient.

        Parameters
        ----------
        username : str
            The message recipient's username.
        string : str
            Some string.

        Returns
        -------
        list
            All messages that contain the string, in their title or body.
        """
        user_box = self.boxes[username]
        return [msg['body'] for msg in user_box if string in msg['title'] or string in msg['body']]


def show_example():
    """Show example of using the PostOffice class."""
    users = ('Newman', 'Mr. Peanutbutter')
    post_office = PostOffice(users)
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_title='first message',
        message_body='Hello, Newman.',
    )
    print(f"Successfuly sent message number {message_id}.")
    print(post_office.boxes['Newman'])
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_title='second message',
        message_body='Hi, Newman.',
    )
    print(post_office.boxes['Newman'])
    print(post_office.search_inbox('Newman', 'message'))
    print(post_office.read_inbox('Newman', 1))
    print(post_office.read_inbox('Newman', 1))
    print(post_office.read_inbox('Newman', 1))


show_example()
