package input

import (
	"fmt"
	"os"

	"github.com/chzyer/readline"
)

func GetExpressionFromStdin() (string, error) {

	var expression string

	rl, err := readline.New("Enter an expression > ")
	if err != nil {
		return "", fmt.Errorf("failed to initialise readline: %w", err)
	}
	defer rl.Close()

	// ? Readline here might be overkill...
	expression, err = rl.Readline()
	if err == readline.ErrInterrupt {
		fmt.Println("Goodbye!")
		os.Exit(0)
	}
	if err != nil {
		return "", fmt.Errorf("failed to read line: %w", err)
	}

	return expression, err

}
