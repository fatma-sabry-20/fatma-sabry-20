import time

class Stage:
    def __init__(self, stage_num, title, story, puzzle, check_function, hint):
        self.stage_num = stage_num
        self.title = title
        self.story = story
        self.puzzle= puzzle
        self.check_function = check_function
        self.hint = hint

class CodingGameEngine:
    def __init__(self, stages, max_attempts=3):
        self.stages = stages
        self.max_attempts = max_attempts
        self.current_stage_index = 0
        self.score = 0

    def start_game(self):
        print("=========================================")
        print("the digital bomb has been activated !!")
        print(" your mission: hack the system and stop the countdown. ")
        print("=========================================\n")
        time.sleep(5)

        while self.current_stage_index < len(self.stages):
            stage = self.stages[self.current_stage_index]
            passed = self.play_stage(stage)

            if not passed:
               print(" !BOOM! the bomb has exploded. try again.\n ")
               return        
          
            self.current_stage_index += 1

        print(" congratulations you've succeeded in stopping the bomb and saving the system. \n ")
        print(f" score : {self.score}")

    def play_stage(self, stage):
         print(f"\n stage :{stage.stage_num}: {stage.title}")
         print(f" story : {stage.story}")
         print(f" puzzle : {stage.puzzle}")

         attempts = 0
         while attempts < self.max_attempts:
            user_input = input(" your answer: ")

            if user_input.lower() == "hint":
                print(f" hint :{stage.hint}") 
                continue
           
            if stage.check_function(user_input):
                print(" correct . move to the next stage. ")
                self.score += (self.max_attempts - attempts) * 10
                return True
            else:
                attempts += 1
                remaining = self.max_attempts - attempts
                print(f" incorrect. you have {remaining} attempts left. ")
                if attempts == self.max_attempts:
                    return False

def check_linear_search(answer):
    return answer == "7" 
      
def check_binary_search(answer):
    return answer == "10"  

def check_sorting(answer):
    return answer == "[12, 25, 43, 89]" 
    
stage1 = Stage( stage_num = 1, title = "linear search",
         story = "you need to find the secret number in an unsorted list.",
         puzzle = "unsorted list: [3, 7, 2, 9, 4, 1, 8, 5, 6]. what is the secret number?",
         check_function = check_linear_search ,
         hint = "the secret number is the one that comes after 3 in the list.")
 
stage2 = Stage( stage_num = 2, title = "binary search", 
        story = "time is running out! the system contians 1024 files sorted alphabetically, and one of them contians the shutdown key. ",
        puzzle = "using binary search algorithm, what is the maximum number of steps needed to find the file ", 
        check_function = check_binary_search, 
        hint = "divide 1024 by 2 repeatedly. how many times can you do that ")

stage3 = Stage( stage_num=3, title="Sorting",
       story = "You reached the core! The wires are encrypted and need to be sorted in ascending order to work properly.",
       puzzle = "Sort this list in ascending order using Python format: [89, 12, 43, 25]",
       check_function = check_sorting,
       hint = "Write the numbers from smallest to largest inside square brackets, like [1, 2, 3, 4].")

game_stages = [stage1, stage2, stage3]
game = CodingGameEngine(stages=game_stages)
game.start_game ()