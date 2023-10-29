#https://leetcode.com/problems/robot-bounded-in-circle/description/?envType=study-plan-v2&envId=programming-skills
def isRobotBounded(self, instructions: str) -> bool:
        direction=((0,1),(1,0),(0,-1),(-1,0))

        position=(0,0)
        point=0

        for i in instructions:
            if i=="G":
                position=(position[0]+direction[point][0],position[1]+direction[point][1])

            elif i =="L":
                point=(point-1)%4
            else:
                point=(point+1)%4

        return position==(0,0) or point!=0