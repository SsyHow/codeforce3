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
	var a, s int
	Fscan(in, &a, &s)
	L := make([]int, a)
	var h, m int
	for i := 0; i < a; i++ {
		Fscan(in, &h, &m)
		L[i] = h*60 + m
	}

	if L[0] >= s+1 {
		Fprintln(out, 0, 0)
	} else {
		f := true
		for i := 0; i < a-1; i++ {
			l := L[i]
			r := L[i+1]
			if f && r-l >= 2*s+2 {
				t := l + s + 1
				Fprintln(out, t/60, t%60)
				f = false
			}
		}
		if f {
			t := L[a-1] + s + 1
			Fprintln(out, t/60, t%60)
		}
	}
}

func main() {
	run(os.Stdin, os.Stdout)
}
