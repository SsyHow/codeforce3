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
	var s string
	Fscan(in, &s)
	L := []rune(s)
	k := 0
	for _, v := range L {
		if v == 'B' {
			k += 1
		}

	}

	if s[b-1] == 'B' && k >= 2 {
		Fprintln(out, "Bob")
	} else if s[0] == 'B' && s[b-2] == 'B' {
		Fprintln(out, "Bob")
	} else {
		Fprintln(out, "Alice")
	}
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a int
	Fscan(in, &a)
	for i := 0; i < a; i++ {
		solve(in, out)
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
