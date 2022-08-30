import streamlit as st
from multiprocessing import Pool, cpu_count
import threading
import time


def func(iterations, id):
    i = 0
    for i in range(iterations):
        i += 1
    print("Finished job id =", id)


if __name__ == "__main__":
    pool = Pool(cpu_count())

    st.title("Speed You Code!")

    jobs_count = 5
    iterations = 10 ** 3
    c1, c2 = st.columns(2)

    with c1:
        if st.button("multiprocess"):
            inputs = [(iterations, i) for i in range(jobs_count)]
            t11 = time.time()
            pool.starmap(func, inputs)
            t21 = time.time()
            st.write(f"Finished after {t21 - t11} seconds")
    with c2:
        if st.button("multithread"):
            threads = [threading.Thread(target=func, args=(iterations, i)) for i in range(10)]

            t12 = time.time()
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
            t22 = time.time()
            st.write(f"Finished after {t22 - t12} seconds")
