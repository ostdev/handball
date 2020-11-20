from django.db import models

# Create your models here.
class Teams:
    def __init__(self):
        self.teams = dict()
    def add_team(self,name):
        t = self.teams.get(name, {'wins':0,'oponents':set()})
        self.teams[name] = t
        return t
    
    def get_score(self,score1,score2):
    	#result[0] = int(score1[0]) > int(score1[1]) + 
        total_points = [int(score1[0]) + int(score2[1]), int(score1[1]) + int(score2[0])]
        print(total_points)
        away_points = [int(score2[0]),int(score1[1])]
        print(away_points)
        if total_points[0] == total_points[1]:
            if away_points[0] > away_points[1]:
                return [1,0]
            else:
                return [0,1]
        elif total_points[0] > total_points[1]:
            return [1,0]
        else:
            return [0,1]

    
    def add_match(self,team1,team2,score1,score2):

        t1 = self.add_team(team1)
        t2 = self.add_team(team2)
        t1['oponents'].add(team2)
        t2['oponents'].add(team1)
        score = self.get_score(score1.split(":"),score2.split(":"))
        t1['wins'] += score[0]
        t2['wins'] += score[1]
        
    
    def __repr__(self):
        sorted_keys = sorted(self.teams.keys(), key = lambda x: (self.teams[x]['wins'], x))
        res = ""
        for key in sorted_keys:
            res += "\n"+key
            res += "\n - Wins: "+str(self.teams[key]['wins'])
            res += "\n - Oponents: "+", ".join(sorted(self.teams[key]['oponents']))
        return res

    def html(self):
        sorted_keys = sorted(self.teams.keys(), key = lambda x: (-self.teams[x]['wins'], x))
        res = ""
        for key in sorted_keys:
            res += "<div>"+key
            res += "<div><span> - Wins: "+str(self.teams[key]['wins'])+"</span></div>"
            res += "<div><span> - Oponents: "+", ".join(sorted(self.teams[key]['oponents']))+"</span></div>"
            res += "</div>"
        return res
