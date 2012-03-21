(defn cross
  ([f xs] xs)
  ([f xs ys] (for [x xs y ys] (f x y)))
  ([f xs ys & more] (apply cross f (cross f xs ys) more)))

(defn dice-distn
  [number sides]
  (frequencies (apply cross + (take number (repeat (range 1 (inc sides)))))))

(defn prob
  [pete colin prob]
  (if (seq pete)
    (let [pete_roll (first (first pete))
          pete_count (second (first pete))
          roll_beat (reduce + (for [[v c] colin :when (> pete_roll v)] c))
          roll_prob (/ roll_beat (Math/pow 6 6))]
      (recur (rest pete) colin (+ prob (/ (* pete_count roll_prob) (Math/pow 4 9)))))
    prob))

(prob (dice-distn 9 4) (dice-distn 6 6) 0)

