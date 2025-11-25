package main

import (
	"bufio"
	. "fmt"
	"io"
	"math"
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
	var a, b float64
	Fscan(in, &a, &b)
	lhs := a * math.Log(b)
	rhs := b * math.Log(a)

	if math.Abs(lhs-rhs) < 1e-12 {
		Fprintln(out, "=")
	} else if lhs > rhs {
		Fprintln(out, "<")
	} else {
		Fprintln(out, ">")
	}
}

func main() {
	run(os.Stdin, os.Stdout)
}
