-- Project Euler problem #205
-- (cc) Arwyn Roberts 2012

-- Peter has 9 4-sided dice (1..4)
-- Colin has 6 6-sided dice (1..6)
-- If they both roll their dice and sum the total, 
-- what is the probability that Peter's score is greater than Colin's?

-- pad puts y zeros either end of xs
pad xs y = zs ++ xs ++ zs
  where zs = replicate y 0 

-- takes sublists of length n from xs (length xs >= n)
-- e.g sublists 2 [1..5] = [[1,2],[2,3],[3,4],[4,5]]
sublists n xs
  | length xs == n = [xs]
  | otherwise = (take n xs):sublists n (tail xs)

-- tricky bit!
-- calculates lists of the relative frequencies of all the possible scores for a dice of d sides 
-- rolled [0..] times and summed (infinite list)
freqs d = iterate roll [1]
  where roll xs = map sum $ sublists d (pad xs (d-1)) 

-- generate a list of pairs (score,prob) for n dice of d sides                        
probs d n = zip [n..] $ map (/ sum fs) fs
  where fs = freqs d !! n

-- sum the combined probability distribution filtered for peter beats colin
e205 = sum [ snd p * snd c | p <- peter, c <- colin, fst p > fst c ]
  where peter = probs 4 9
        colin = probs 6 6
