class BowlingGame:
    def __init__(self):
        # Initialize an empty list to store shots
        self.shots = []
        # Initialize an empty list to store frames
        self.frames = []

    def roll(self, pins):
        # Check if the number of pins is valid
        if not 0 <= pins <= 10:
            raise IndexError("cannot throw bonus with an open tenth frame")
        # Append the number of pins to the shots list
        self.shots.append(pins)

        # If there are no frames, add a new frame and append the pins to it
        if not self.frames:
            self.frames.append([pins])
        else:
            # If the last frame is not complete
            if len(self.frames[-1]) < 2:
                # Check if the sum of the pins is greater than 10
                if self.frames[-1][0] != 10 and self.frames[-1][0] + pins > 10:
                    raise ValueError("invalid fill balls")
            # If the current roll is a strike, add a new frame
            if pins == 10 and len(self.frames) < 10:
                self.frames.append([pins])
            else:
                # If this is the last frame, check if it's complete
                if len(self.frames) == 10:
                    # raises an error if the frame already has 3 elements
                    if len(self.frames[-1]) == 3:
                        raise ValueError("invalid fill balls")
                    # raises an error if the frame is complete
                    if len(self.frames[-1]) == 2 and sum(self.frames[-1]) == 0:
                        raise ValueError("invalid fill balls")
                    if len(self.frames[-1]) == 2 and 10 < sum(self.frames[-1]) < 20:
                        # If the last frame is a spare and this is the first fill ball, check if the next roll is valid
                        if self.frames[-1][0] == 10:
                            if self.frames[-1][1] + pins > 10:
                                raise ValueError("invalid fill balls")
                            else:
                                self.frames[-1].append(pins)
                        else:
                            self.frames[-1].append(pins)
                    else:
                        self.frames[-1].append(pins)
                # If this is not the last frame, add the pins to the current frame
                elif len(self.frames[-1]) < 2 and self.frames[-1][0] < 10:
                    self.frames[-1].append(pins)
                else:
                    self.frames.append([pins])
        return

    def score(self):
        # Check if there are at least 10 frames in the game
        if len(self.frames) < 10:
            raise IndexError("cannot throw bonus with an open tenth frame")

        # stores the score of the pins
        pins_score = 0
        # stores the index of the shots that should count double
        bonus_index = []
        # get the score of the first 9 frames
        first_frames = self.frames[:-1]
        # stores current index
        shot_index = 0

        # Loop over the first 9 frames of the game
        for frame in first_frames:
            # Get the pins knocked down in the first and second shot of the frame
            first, *second = frame
            # If the first shot was a strike, add 10 points to the score and mark the next two shots as bonus
            if first == 10:
                pins_score += 10
                bonus_index.extend([shot_index + 1, shot_index + 2])
            else:
                # If the second shot exists, add the sum of the first and second shot to the score
                if len(second):
                    pins_score += first + second[0]
                    # If the sum of the first and second shot is a spare, mark the next shot as bonus
                    if first + second[0] == 10:
                        bonus_index.append(shot_index + 2)
            # Update the shot index with the length of the current frame
            shot_index += len(frame)

        # Get the pins knocked down in the last frame of the game
        last_shot = self.frames[-1]
        # Get the pins knocked down in the first, second and third (if exists) shot of the last frame
        first, second, *third = last_shot
        # If the first shot was a strike or the sum of the first and second shot was a spare, add the pins knocked down in the third shot to the score
        if first == 10 or first + second == 10:
            pins_score += first + second + third[0]
        else:
            # Otherwise, add the sum of the first and second shot to the score
            pins_score += first + second

        # Get the bonus pins knocked down in the game
        bonus_pins_lst = [self.shots[i] for i in bonus_index]
        # Add the bonus pins to the score
        pins_score += sum(bonus_pins_lst)
        return pins_score
