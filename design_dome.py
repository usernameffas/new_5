import numpy as np

def load_csv(filename):
    try:
        arr = np.loadtxt(filename, delimiter=',', skiprows=1)
        return arr
    except FileNotFoundError as e:
        print('오류: 파일을 찾을 수 없습니다 -', e)
        exit(1)
    except Exception as e:
        print('CSV 파일 로드 오류:', e)
        exit(1)

def main():
    arr1 = load_csv('mars_base_main_parts-001.csv')
    arr2 = load_csv('mars_base_main_parts-002.csv')
    arr3 = load_csv('mars_base_main_parts-003.csv')

    parts = np.concatenate((arr1, arr2, arr3), axis=0)
    mean_values = np.mean(parts, axis=1)
    parts_below_50_mask = mean_values < 50
    parts_to_work_on = parts[parts_below_50_mask]

    try:
        np.savetxt('parts_to_work_on.csv', parts_to_work_on, delimiter=',', fmt='%.6f')
        print('parts_to_work_on.csv 파일 저장 성공')
    except Exception as e:
        print('parts_to_work_on.csv 저장 오류:', e)
        exit(1)

    print('전체 분석된 부품 수:', parts.shape)
    print('평균 < 50인 부품 수:', parts_to_work_on.shape)
    print('전체 부품 평균 강도: %.2f' % np.mean(parts))
    print('보강이 필요한 부품 비율: %.1f%%' % ((parts_to_work_on.shape / parts.shape) * 100))

    # Bonus Task
    try:
        parts2 = np.loadtxt('parts_to_work_on.csv', delimiter=',')
        parts3 = np.transpose(parts2)
        print('전치행렬(parts3):\n', parts3)
    except Exception as e:
        print('Bonus 파일 처리 오류:', e)
        exit(1)

if __name__ == '__main__':
    main()
