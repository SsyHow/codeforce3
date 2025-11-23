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
	var a, k int
	Fscan(in, &a, &k)
	L := make([]int, a)
	summ := 0
	for i := 0; i < a; i++ {
		Fscan(in, &L[i])
		summ += L[i]
	}
	if summ%k > 0 {
		Fprintln(out, "No")
	} else {
		x := summ / k
		tmp := 0
		ans := make([]int, 0)
		cnt := 0
		for i := 0; i < a; i++ {
			tmp += L[i]
			cnt += 1
			if tmp == x {
				ans = append(ans, cnt)
				cnt = 0
				tmp = 0
			} else if tmp > x {
				Fprintln(out, "No")
				return
			}
		}
		Fprintln(out, "Yes")
		for _, v := range ans {
			Fprint(out, v, " ")
		}
		Fprintln(out)
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
