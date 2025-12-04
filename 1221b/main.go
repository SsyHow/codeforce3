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
	f := true

	for i := 0; i < a; i++ {
		if f {
			for j := 0; j < a/2; j++ {
				Fprint(out, "WB")
			}
			if a%2 == 1 {
				Fprint(out, "W")
			}
			Fprintln(out)
		} else {
			for j := 0; j < a/2; j++ {
				Fprint(out, "BW")
			}
			if a%2 == 1 {
				Fprint(out, "B")
			}
			Fprintln(out)
		}
		f = !f
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
