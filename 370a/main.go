package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func abs(x int) int {
	if x < 0 {
		return -x

	}
	return x
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var r1, c1, r2, c2 int
	Fscan(in, &r1, &c1, &r2, &c2)

	rook := 2
	if r1 == r2 || c1 == c2 {
		rook = 1
	}
	bishop := 0
	if (r1-c1)&1 == (r2-c2)&1 {
		bishop = 2
		if abs(r2-r1) == abs(c2-c1) {
			bishop = 1
		}
	}

	king := max(abs(r1-r2), abs(c1-c2))
	Fprintln(out, rook, bishop, king)

}

func main() {
	run(os.Stdin, os.Stdout)
}
