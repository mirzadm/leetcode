from typing import List, Set


def find_number_of_friends_circles(friends_matrix: List[List[int]]) -> int:
    """Finds number of friends circles in a given a friendship matrix.
    
    Example:
        friends_matrix = [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 1],
        ]
        There are two friends circles: {0, 1}, {2}

    Args:
        `friends_matrix`: A binary square matrix representing friendships.
    Returns:
        Number of friends circles.
    """
    number_of_students = len(friends_matrix)
    to_visit = set(range(number_of_students))
    friends_circles = []
    while to_visit:
        next_student = to_visit.pop()
        friends_circle = find_friends_circle(friends_matrix, next_student)
        to_visit -= friends_circle
        friends_circles.append(friends_circle)
    return len(friends_circles)


def find_friends_circle(friends_matrix: List[List[int]], student: int) -> Set[int]:
    """Finds friends circle of a given student.

    Implements a search through friendship graph in no particular order.

    Example:
        friends_matrix = [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 1],
        ]
        Friends circle of 0 is {0, 1} and friends circle of 2 is {2}.
    Args:
        `friends_matrix`: A binary square matrix representing friendships.
        `student`: Non-negative integer index of a student
    Returns:
        Set of friends.
    """
    number_of_students = len(friends_matrix)
    to_visit = set([student])
    friends_circle = set()
    while to_visit:
        next_student = to_visit.pop()
        friends_circle.add(next_student)
        for student in range(number_of_students):
            if friends_matrix[next_student][student]:
                if student not in to_visit and student not in friends_circle:
                    to_visit.add(student)
    return friends_circle
    