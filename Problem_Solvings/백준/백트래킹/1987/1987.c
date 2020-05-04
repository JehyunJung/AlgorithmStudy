#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define TRUE 1
#define FALSE 0

int max_distance = 1;
char** arrays;
char path[27];

int dir_x[4] = { 0,1,0,-1 };
int dir_y[4] = { -1,0,1,0 };
int n_rows, n_cols;

int promising(char next_path, int distance) {
	int i;
	for (i = 0; i < distance; i++) {
		if (path[i] == next_path)
			return FALSE;
	}
	return TRUE;
}

void dfs(int current_row, int current_col, int distance) {
	int i, next_row, next_col;
	char next_char;
	if (distance > max_distance)
		max_distance = distance;

	for (i = 0; i < 4; i++) {
		next_row = current_row + dir_y[i];
		next_col = current_col + dir_x[i];

		if (next_row >= 0 && next_row < n_rows && next_col >= 0 && next_col < n_cols) {
			next_char = arrays[next_row][next_col];
			if (promising(next_char, distance)) {
				path[distance] = next_char;
				dfs(next_row, next_col, distance + 1);
			}

		}
	}
	return;
}
int main(void) {
	int i, num;
	scanf("%d %d", &n_rows, &n_cols);
	arrays = (char**)malloc(sizeof(char*)*n_rows);
	for (i = 0; i < n_rows; i++) {
		arrays[i] = (char*)malloc(sizeof(char)*n_cols);
		scanf("%s", arrays[i]);
	}
	path[0] = arrays[0][0];
	dfs(0, 0, 1);
	printf("%d", max_distance);

	for (i = 0; i < n_rows; i++)
		free(arrays[i]);
	free(arrays);
}