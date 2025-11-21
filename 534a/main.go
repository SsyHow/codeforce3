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
	var a int
	Fscan(in, &a)

	if a == 2 {
		Fprintln(out, "1\n1")
	} else if a == 3 {
		Fprintln(out, "2\n1 3")
	} else {
		L := make([]int, 0, a)
		for i := 2; i <= a; i += 2 {
			L = append(L, i)
		}
		for i := 1; i <= a; i += 2 {
			L = append(L, i)
		}

		Fprintln(out, a)
		for _, v := range L {
			Fprint(out, v, " ")
		}
		Fprintln(out)

	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
