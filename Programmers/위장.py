def solution(genres, plays):
    answer = []
    song, total_play = {}, {}
    
    for i in range(len(plays)):
        if genres[i] in song:
            song[genres[i]].append((plays[i], i))
        else:
            song[genres[i]] = [(plays[i], i)]
        
        if genres[i] in total_play:
            total_play[genres[i]] += plays[i]
        else:
            total_play[genres[i]] = plays[i]
    
    total_play = sorted(total_play, key=lambda x:(-total_play[x]))
    
    for t in total_play:
        temp = sorted(song[t], key=lambda x:-x[0])
        answer.append(temp.pop(0)[1])
        if temp:
            answer.append(temp.pop(0)[1])
    
    return answer
