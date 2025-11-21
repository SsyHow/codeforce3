package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var b int
	Fscan(in, &b)
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()

	L := make([][]int, 3)
	for i := range L {
		L[i] = make([]int, 3)
	}
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			Fscan(in, &L[i][j])
		}
	}

	k := (L[0][2] + L[2][0]) / 2
	L[0][0] = k - (L[0][1]-L[1][2])/2
	L[2][2] = k*2 - L[0][0]
	L[1][1] = L[0][0] + L[0][1] + L[0][2] - k*2
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			Fprint(out, L[i][j], " ")
		}
		Fprintln(out)
	}
}

func main() {
	run(os.Stdin, os.Stdout)
}
