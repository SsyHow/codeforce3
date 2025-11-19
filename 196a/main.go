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
	var s string
	Fscan(in, &s)

	L := []rune{}

	for i := 0; i < len(s); i++ {
		if len(L) == 0 || L[len(L)-1] >= rune(s[i]) {
			L = append(L, rune(s[i]))
		} else {
			for len(L) > 0 && L[len(L)-1] < rune(s[i]) {
				L = L[:len(L)-1]
			}
			L = append(L, rune(s[i]))
		}
	}
	Fprintln(out, string(L))
}

func main() {
	run(os.Stdin, os.Stdout)
}
