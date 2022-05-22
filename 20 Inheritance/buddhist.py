import random
import errors


class Buddhist:
    def __init__(self):
        self.karma = 0

    def one_day(self):
        try:
            if random.randint(1, 10) == 1:
                raise errors.KillError
            elif random.randint(1, 10) == 2:
                raise errors.DrunkError
            elif random.randint(1, 10) == 3:
                raise errors.CarCrashError
            elif random.randint(1, 10) == 4:
                raise errors.GluttonyError
            elif random.randint(1, 10) == 5:
                raise errors.DepressionError
            else:
                self.karma += random.randint(1, 7)
        except errors.KillError:
            with open('karma.log', 'a') as ouf:
                ouf.write('KillError \n')
        except errors.DepressionError:
            with open('karma.log', 'a') as ouf:
                ouf.write('DepressionError \n')
        except errors.DrunkError:
            with open('karma.log', 'a') as ouf:
                ouf.write('DrunkError \n')
        except errors.CarCrashError:
            with open('karma.log', 'a') as ouf:
                ouf.write('CarCrashError \n')
        except errors.GluttonyError:
            with open('karma.log', 'a') as ouf:
                ouf.write('GluttonyError \n')

