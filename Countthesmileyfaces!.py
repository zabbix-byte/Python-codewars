'''
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

Example
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
Note
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.
'''
import unittest


def count_smileys(arr):
    counter = 0

    for i in arr:
        valid = True
        nose = False

        if i[0] not in [':', ';']:
            valid = False
        
        if len(i) == 3:
            nose = True

        if nose:
            if i[1] not in ['-', '~']:
                valid = False
            if i[2] not in [')', 'D']:
                valid = False
        else:
            if i[1] not in [')', 'D']:
                valid = False
        
        if valid:
            counter+=1

    return counter


class TestCountSmileys(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(count_smileys([]), 0)
        self.assertEqual(count_smileys([':D',':~)',';~D',':)']), 4)
        self.assertEqual(count_smileys([':)',':(',':D',':O',':;']), 2)
        self.assertEqual(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)


if __name__ == '__main__':
    unittest.main()
