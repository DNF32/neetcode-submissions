func groupAnagrams(strs []string) [][]string {
    output:= make(map[[26]int][]string)

    for _, str :=range strs{
        updateMap(output,str)
    }
    res := make([][]string, 0, len(output))

    for _, group := range output {
        res = append(res, group)
    }
    
    return res
}

func updateMap(anagrams map[[26]int][]string, potencial string){
       arr:= strToArray(potencial) 
       _, ok:= anagrams[arr]
       if !ok{
            anagrams[arr] =[]string{potencial}
            return 
       }
       anagrams[arr] = append(anagrams[arr],potencial)
}


func strToArray(s string) [26]int {
    var out [26]int

    for _, r := range s {
        out[r-'a']++
    }

    return out
}

func isAnagram(s string, t string) bool {
    sSet := make(map[rune]int) 
    tSet := make(map[rune]int) 

    for _, char:= range s{
        sSet[char] +=1
    }
    for _, char:= range t{
        tSet[char] +=1
    }

    if len(sSet) != len(tSet){
        return false
    }
    for key,value := range sSet{
        val, ok := tSet[key]
        if !ok{
            return false
        }
        if val !=value{
            return false
        }
    }

     for key,value := range tSet{
        val, ok := sSet[key]
        if !ok{
            return false
        }
        if val !=value{
            return false
        }
    }
    return true
}
