def update_scores(teams, team_a, team_b, res):
    if res == 'win':
        teams.update({team_a: [teams[team_a][0]+1, teams[team_a][1]+1, teams[team_a][2], teams[team_a][3],teams[team_a][4]+3]})
        teams.update({team_b: [teams[team_b][0]+1, teams[team_b][1], teams[team_b][2], teams[team_b][3]+1,teams[team_b][4]]})
    if res == 'loss':
        teams.update({team_a: [teams[team_a][0]+1, teams[team_a][1], teams[team_a][2], teams[team_a][3]+1,teams[team_a][4]]})
        teams.update({team_b: [teams[team_b][0]+1, teams[team_b][1]+1, teams[team_b][2], teams[team_b][3],teams[team_b][4]+3]})
    if res == 'draw':
        teams.update({team_a: [teams[team_a][0]+1, teams[team_a][1], teams[team_a][2]+1, teams[team_a][3],teams[team_a][4]+1]})
        teams.update({team_b: [teams[team_b][0]+1, teams[team_b][1], teams[team_b][2]+1, teams[team_b][3],teams[team_b][4]+1]})
    
    
def build_table(teams):
    
    table = ["Team                           | MP |  W |  D |  L |  P"]
    
    if ( teams != {} ):
        
        teams_list = [team for team in teams]
        teams_list_sorted = []
        
        next_team = teams_list[0]
        length = len(teams_list)
        
        while ( len(teams_list) > 0 ) :
            
            next_team = teams_list[0]
            
            for team in teams_list:
                
                if teams[team][4] > teams[next_team][4]:
                    next_team = team
                    
                elif teams[team][4] == teams[next_team][4]:
                    if ( team[0] < next_team[0] ):
                        next_team = team
                        
            teams_list_sorted.append(next_team)
            teams_list.remove(next_team)
            
        for team in teams_list_sorted:
          row = team.ljust(31) + f'|  {teams[team][0]} |  {teams[team][1]} |  {teams[team][2]} |  {teams[team][3]} |  {teams[team][4]}'
          table.append(row)
          
    return table


def tally(rows):
    
    team_a = ''
    team_b = ''
    res = ''
    teams = {}
    
    for result in rows:
        result_split = result.split(';')
        team_a = result_split[0]
        team_b = result_split[1]
        res = result_split[2]
        
        if (team_a not in teams):
            teams.update({team_a:[0,0,0,0,0]})
            
        if (team_b not in teams):
            teams.update({team_b:[0,0,0,0,0]})
            
        update_scores(teams, team_a, team_b, res)
    
    table = build_table(teams)
    
    return table     

