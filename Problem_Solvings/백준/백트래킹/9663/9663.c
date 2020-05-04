#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define TRUE 1
#define FALSE 0

int count = 0;
int *rows;
int promising(int current_row, int next_column) {
	int i = 0;
	int next_row = current_row;
		for (i = 0; i < current_row; i++) {
			if (rows[i] == next_column || next_row - i == abs(rows[i] - next_column))
				return FALSE;
		}
	return TRUE;
}

void nqueens(int num, int current_row) {
	int i = 0;
		if (current_row == num) {
			count += 1;
			return;
		}
	for (i = 0; i < num; i++) {
		if (promising(current_row, i)) {
			rows[current_row] = i;
			nqueens(num, current_row + 1);
			rows[current_row] = 0;
		}
	}
}
int main(void) {
	int i, num;
	scanf("%d", &num);
	rows = (int*)malloc(sizeof(int)*(num));
	for (i = 0; i < num; i++)
		rows[i] = 0;
	nqueens(num,0);
	printf("%d", count);
	free(rows);
}