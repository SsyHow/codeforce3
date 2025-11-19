package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var l1, r1, l2, r2, k int
	Fscan(in, &l1, &r1, &l2, &r2, &k)
	l := max(l1, l2)
	rr := min(r1, r2)

	if l <= k && k <= rr {
		Fprintln(out, max(rr-l, 0))
	} else {
		Fprintln(out, max(rr-l+1, 0))
	}
}

func main() {
	run(os.Stdin, os.Stdout)
}
