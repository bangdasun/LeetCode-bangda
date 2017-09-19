/*
  https://leetcode.com/problems/reshape-the-matrix/description/
*/

public class ReshapeMatrix {
  public static int[][] matrixReshape(int[][] nums, int r, int c) {
    
    if (nums.length * nums[0].length != r * c) {
      return nums;
    }
    
    int x = 0, y = 0;
    int rC = nums[0].length;
    int[][] reshaped = new int[r][c];
    
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        
        reshaped[i][j] = nums[x][y];
        
        // origin matrix "run out of" columns, start from next row
        if (y >= rC - 1) {
          y = 0;
          x += 1;
        }
        else {
          // if not, just increase column index of original matrix
          y += 1;
        }
      }
    }
    
    return reshaped;
  }

  public static void main(String[] args) {
    
    //int[][] nums = {{1, 1, 1, 1},
    //                {4, 4, 4, 4},
    //                {6, 6, 6, 6}};
    
    int[][] nums = {{1, 2, 3, 4, 5}};
    
    int[][] reshaped = matrixReshape(nums, 5, 1);
    
    for (int i = 0; i < reshaped.length; i++) {
      for (int j = 0; j < reshaped[0].length; j++) {
        System.out.println(reshaped[i][j]);
      }
      System.out.println("row ends here");
    }
   
  }
}