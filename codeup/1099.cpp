#include <iostream>

int main()
{
  int maze[10][10];
  for (int i = 0; i < 10; i++)
  {
    for (int j = 0; j < 10; j++)
    {
      std::cin >> maze[i][j];
    }
  }

  int x = 1, y = 1;

  while(true)
  {
    if (maze[x][y] == 2)
    {
      maze[x][y] = 9;
      break;
    }

    maze[x][y] = 9;
    if (maze[x+1][y] == 1 && maze[x][y+1] == 1)
      break;

    if (maze[x][y+1] != 1)
      y++;
    else
      x++;
  }

  for (int i = 0; i < 10; i++)
  {
    for (int j = 0; j < 10; j++)
    {
      std::cout << maze[i][j] << ' ';
    }
    std::cout << '\n';
  }

  return 0;
}