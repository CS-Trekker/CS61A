"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    index = -1
    for i in paragraphs:
            if select(i):
                index += 1
                if index == k:
                    return i
    return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.
    实现about，它接受一个主题词列表。它返回一个函数，该函数接受一个段落，并返回一个布尔值，指示该段落是否包含topic中的任何单词。返回的函数可以作为select参数传递给choose。 为了准确地进行比较，您需要忽略段落中的大小写（即假设大写和小写字母不会改变它是什么单词）和标点符号。 假设主题列表中的所有单词都是小写的，并且不包含标点符号。 
    提示：您可以使用utils.py中的字符串实用程序函数

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def func(paragraphs):
        for i in split(paragraphs):
            i = lower(remove_punctuation(i))
            if i in topic:
                return True
        return False
    return func
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.
    实现accuracy，它接受一个类型化段落和一个引用段落。它返回与引用中相应单词完全匹配的键入单词的百分比。大小写和标点也必须匹配。 在此上下文中，单词是用空格与其他单词隔开的任何字符序列，因此将“dog；”视为一个单词。 如果一个键入的单词在引用中没有对应的单词，因为typed比reference长，那么typed中的额外单词都是不正确的。 如果type为空，则accuracy为零。

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if len(typed_words) == 0:
        return 0.0
    elif len(typed_words) > len(reference_words):
        correct_count = 0
        for i in range(len(reference_words)):
            if typed_words[i] == reference_words[i]:
                correct_count += 1
        return correct_count / len(typed_words) * 100.0
    else:
        correct_count = 0
        for i in range(len(typed_words)):
            if typed_words[i] == reference_words[i]:
                correct_count += 1
        return correct_count / len(typed_words) * 100.0
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.
    实现wpm，在给定键入的字符串typed和以秒为单位的经过时间elapsed的情况下，计算每分钟的字数（打字速度的度量）。尽管它的名字是“每分钟字数”，但它不是基于输入的单词数，而是基于字符数，因此打字测试不会受到单词长度的影响。每分钟字数的公式是输入的字符数（包括空格）除以5（典型的单词长度）与所用时间（以分钟为单位）的比率。 例如，字符串“I am glad!”包含三个单词和十个字符（不包括引号）。每分钟字数计算使用2作为输入的字数（因为10 / 5 = 2）。如果有人在30秒（半分钟）内输入这个字符串，他们的速度将是每分钟4个单词.
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) / 5 / elapsed * 60
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    实现自动更正，它接受一个user_word、一个valid_words列表、一个diff_function和一个limit。 如果user_word包含在valid_words列表中，则自动更正返回该单词。否则，根据diff_function，自动更正将返回valid_words中与提供的user_word差异最小的单词。但是，如果user_word和任何valid_words之间的最小差值大于limit，则返回user_word。 diff函数接受三个参数。前两个参数是要比较的两个字符串（user_word和valid_words中的一个单词），第三个参数是限制。diff函数的输出是一个数字，表示两个字符串之间的差值。
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    else:
        lowest_diff_value = 100000000000000000000
        lowest_diff_word = user_word
        for word in valid_words:
            diff_value = diff_function(user_word, word, limit)
            if diff_value <= limit and diff_value < lowest_diff_value:
                lowest_diff_word = word
                lowest_diff_value = diff_value
        return lowest_diff_word
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    实现shifty_shifts，这是一个diff函数，接受两个字符串。它返回将开始单词转换为目标单词必须更改的最小字符数。如果两个字符串的长度不相等，则将长度之差加到总数中。
    重要：您不能在实现中使用while或for语句。使用递归。
    """
    # BEGIN PROBLEM 6
    def helper(start, goal, diff):
        if diff > limit:
            return limit + 1
        elif len(start) == 0 or len(goal) == 0:
            return diff + abs(len(start) - len(goal))
        else:
            if start[0] == goal[0]:
                return helper(start[1:], goal[1:], diff)
            else:
                return helper(start[1:], goal[1:], diff + 1)
    return helper(start, goal, 0)
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # if ______________: # Fill in the condition
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END

    # elif ___________: # Feel free to remove or add additional cases
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END

    # else:
    #     add_diff = ... # Fill in these lines
    #     remove_diff = ...
    #     substitute_diff = ...
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END
    original_limit = limit
    if limit < 0:# Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return original_limit + 1
        # END

    elif len(start) == 0 or len(goal) == 0: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(start) + len(goal)
        # END
        
    elif start[0] == goal[0]:
        return pawssible_patches(start[1:], goal[1:], limit)

    else:
        add_diff = pawssible_patches(start, goal[1:], limit - 1)
        remove_diff = pawssible_patches(start[1:], goal, limit - 1)
        substitute_diff = pawssible_patches(start[1:], goal[1:], limit -1)
        # BEGIN
        "*** YOUR CODE HERE ***"
        return min(add_diff, remove_diff, substitute_diff) + 1
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    correct_count = 0
    for i in range(min(len(typed), len(prompt))):
        if typed[i] == prompt[i]:
            correct_count += 1
        else:
            break
    progress = correct_count / len(prompt)
    report = {'id': user_id, 'progress': progress}
    send(report)
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    player_num = len(times_per_player)
    times_per_player_per_word = [[] for _ in range(player_num)]
    for i in range(player_num):
        for j in range(len(times_per_player[i]) - 1):
            times_per_player_per_word[i].append(times_per_player[i][j + 1] - times_per_player[i][j])
    return game(words, times_per_player_per_word)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    fastest_list = [[] for _ in player_indices]
    for word_index in word_indices:
        for player_index in player_indices:
            if time(game, player_index, word_index) == min([time(game, i, word_index) for i in player_indices]):
                fastest_list[player_index].append(word_at(game, word_index))
                break
    return fastest_list
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)