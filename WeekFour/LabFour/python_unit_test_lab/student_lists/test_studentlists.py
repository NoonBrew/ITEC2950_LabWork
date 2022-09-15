"""
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

"""

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_cant_create_class_with_negative_students(self):
        with self.assertRaises(StudentError):
            test_class = ClassList(-1)

    def test_cant_create_class_with_zero_students(self):
        with self.assertRaises(StudentError):
            test_class = ClassList(-0)

    # Personally I think this test is helpful for early stages of development to help make sure
    # the list is being created, but at the stage the code was at when this test was introduced
    # it has diminishing returns since all the other tests are making positive lists.
    def test_can_create_class_with_positive_number_of_students(self):
        test_class = ClassList(1)

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


    def test_add_remove_student_ensure_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)


    def test_adds_students_than_removes_student_not_in_classlist(self):
        test_class = ClassList(4)
        test_class.add_student('Justin Jefferson')
        test_class.add_student('Najee Harris')
        test_class.add_student('Antonio Gibbson')
        with self.assertRaises(StudentError):
            test_class.remove_student('Elijah Mitchell')


    def test_removes_student_from_empty_classlist(self):
        test_class = ClassList(4)
        with self.assertRaises(StudentError):
            test_class.remove_student('Josh Jacobs')


    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    def test_is_enrolled_for_student_not_enrolled_in_classlist(self):
        test_class = ClassList(3)
        test_class.add_student('Miles Sanders')
        test_class.add_student('Kenith Gainwell')
        test_class.add_student('Boston Scott')
        self.assertFalse(test_class.is_enrolled('Jalen Hurts'))


    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))
        # Not sure if you want us to edit this redudency or remove it? Is this just for example?

  
    def test_index_of_student_is_none_if_classlist_is_empty(self):
        test_class = ClassList(3)
        index = test_class.index_of_student('Test Student')
        self.assertIsNone(index)
 
 
    
    def test_index_of_student_is_none_if_classlist_not_empty_and_student_not_in_classlist(self):
        test_class = ClassList(4)
        test_class.add_student('Tom Brady')
        test_class.add_student('Mike Evans')
        test_class.add_student('Chris Godwin')
        self.assertIsNone(test_class.index_of_student('Julio Jones'))
   
    
    def test_is_class_full_when_class_is_full(self):
        test_class = ClassList(2)
        test_class.add_student('Malcom Rodrigo')
        test_class.add_student('Adian Hutchinson')
        self.assertTrue(test_class.is_class_full())
    
    
    def test_is_class_full_when_class_is_empty(self):
        test_class = ClassList(3)
        self.assertFalse(test_class.is_class_full())
