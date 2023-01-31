#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - a function that creates an infinite loop to make
 * a program stall
 *
 * Return: 0 (Always for success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - crates 5 zombie processes
 *
 * Return: 0 (Always for success)
 */
int main(void)
{
	int i;
	pid_t Zombie;

	for (i = 0; i < 5; i++)
	{
		Zombie = fork();
		if (!Zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", Zombie);
	}
	infinite_while();
	return (0);
}
