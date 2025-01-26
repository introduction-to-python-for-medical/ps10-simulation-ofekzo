import copy

def spread_fire(grid):
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)  # יצירת עותק של הרשת לשם עדכון

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:  # אם יש עץ בתא הנוכחי
                # יצירת רשימה של שכנים אפשריים, תוך כדי בדיקת גבולות
                neighbors = []
                if i > 0:  # אם לא על גבול העליון
                    neighbors.append(grid[i-1][j])
                if i < grid_size - 1:  # אם לא על גבול התחתון
                    neighbors.append(grid[i+1][j])
                if j > 0:  # אם לא על גבול השמאלי
                    neighbors.append(grid[i][j-1])
                if j < grid_size - 1:  # אם לא על גבול הימני
                    neighbors.append(grid[i][j+1])

                # אם אחד מהשכנים הוא אש (2), התפשטה האש לתא הנוכחי
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid

