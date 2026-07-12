"""
    hello world, this module offers you a very special function where Bob is a lackadaisical teenager. 
"""
def response(hey_bob):
    """
        Function that Bob is a lackadaisical teenager.

        Parameters:
            hey_bob(str): the message you are offering bob.

        Returns:
            Bob is a lackadaisical teenager.
    """
    if hey_bob.strip().endswith('?') and hey_bob.isupper():
        return 'Calm down, I know what I\'m doing!'
    if hey_bob.strip().endswith('?'):
        return 'Sure.'
    if hey_bob.isspace() or len(hey_bob) == 0:
        return 'Fine. Be that way!'
    if hey_bob.isupper():
        return 'Whoa, chill out!'
    return 'Whatever.'
    
