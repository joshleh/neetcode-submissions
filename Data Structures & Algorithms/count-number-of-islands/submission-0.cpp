class Solution {
public:
    void dfs(vector<vector<char>>& grid, int row, int col)
    {
        // Base cases for recursive DFS

        // Out of bounds
        if (row < 0 || row >= grid.size() ||
            col < 0 || col >= grid[0].size())
        {
            return;  
        }
        
        // Water or already visited land
        if (grid[row][col] == '0')
        {
            return;
        }

        // Mark current land as visited
        grid[row][col] = '0';

        // Explore neighbors
        dfs(grid, row + 1, col); // down
        dfs(grid, row - 1, col); // up
        dfs(grid, row, col + 1); // right
        dfs(grid, row, col - 1); // left
    }

    int numIslands(vector<vector<char>>& grid) {
        int islands = 0;

        for (int row = 0; row < grid.size(); row++)
        {
            for (int col = 0; col < grid[0].size(); col++)
            {
                if (grid[row][col] == '1')
                {
                    islands++;
                    dfs(grid, row, col);
                }
            }
        }

        return islands;
    }

};