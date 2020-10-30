#ifndef CONTORL
#define CONTORL

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void clear()
{
	printf("\033[2J");
}

void move_up(int x)
{
	printf("\033[%dA", x);
}

void move_down(int x)
{
	printf("\033[%dB", x);
}

void move_left(int y)
{
	printf("\033[%dD", y);
}

void move_right(int y)
{
	printf("\033[%dC", y);
}

void move_to(int x, int y)
{
	printf("\033[%d;%dH", x, y);	
}

void reset_cursor()
{
	printf("\033[H");
}

void hide_cursor()
{
	printf("\033[?25l");
}

void show_cursor()
{
	printf("\033[?25h");
}

void hight_light()
{
	printf("\033[7m");
}

void un_hight_light()
{
	printf("\033[27m");
}

#endif
