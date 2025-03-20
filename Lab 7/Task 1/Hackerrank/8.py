if __name__ == '__main__':
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    unique_scores = list(set(arr))
    
    if len(unique_scores) > 1:
        unique_scores.sort()  
        print(unique_scores[-2])  
    else:
        print("No runner-up score")
