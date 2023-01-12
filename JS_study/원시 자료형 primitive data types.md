## 자바스크립트의 **원시 자료형** *primitive data types*



typeof 연산자를 이용해 자료형 반환

```javascript
const a = true, b = 123.45, c = '안녕하세요!';

console.log(a, typeof a);
console.log(b, typeof b);
console.log(c, typeof c); 

// true 'boolean'
// 123.45 'number'
// 안녕하세요! string
```



```javascript
let d;
console.log(d, typeof d);
// undefined 'undefined'

d = null;
console.log(d, typeof d); // ⚠️ 'object' 반환
// null 'object'

const e = Symbol('hello');
console.log(typeof e);
// symbol
```



### 1. 불리언 *boolean*

```javascript
let isEmployed = true;
let isMarried = false;

console.log('직업 있음:', isEmployed);
console.log('기혼:', isMarried); 
// 직업 있음: true
// 기혼: false
```



### 2. 숫자 *number*

```javascript
let integer = 100;
let real = 12.34;
let negative = -99;

console.log(integer, real, negative); 
// 100 12.34 -99
```

- 자바스크립트에는 정수와 실수의 구분이 없음 - *정수도 실수로 처리*
- 정수는 `2^53 - 1`까지 안정적으로 표현 가능 - *더 큰 정수는 이후 배울 BigInt로*



### 3. 문자열 *string*

```javascript
let first_name = "Brendan";
let last_name = 'Eich';
let description = `미국의 프로그래머로
자바스크립트 언어를 만들었으며
모질라의 CEO와 CTO를 역임했다.`;

console.log(first_name, last_name);
console.log(description); 
```

- 큰따옴표, 작은따옴표, 또는 백틱으로 둘러싸인 텍스트 데이터

```javascript
console.log(
  typeof (typeof true),
  typeof (typeof 123.45),
  typeof (typeof 'Hello'),
); 
// string string string
```

- 💡 `typeof`의 반환값은 문자열



### 4. undefined

```javascript
let x;
console.log(typeof x);
```

![](C:\Users\justi\AppData\Roaming\marktext\images\2023-01-12-20-24-52-image.png)

- 값이 **부여되지 않은** 상태라는 의미
- ⭐️ 그러나 `undefined`도 **값**임 *많은 다른 언어들과 다른 점*
- 아무 것도 반환하지 않는 구문 - `undefined` 반환

```javascript
let x = 1;
// undefined
```



### 5. null

```javascript
let x;
console.log('값 넣기 전', typeof x);
// 값 넣기 전 undefined

x = null;
console.log('null값 넣은 후', typeof x);
// null값 넣은 후 object

```

![](C:\Users\justi\AppData\Roaming\marktext\images\2023-01-12-20-27-15-image.png)

```javascript
let x = 1;
console.log('변경 전', x);
// 변경 전 1

x = null;
console.log('변경 후', x);
// 변경 후 null
```

![](C:\Users\justi\AppData\Roaming\marktext\images\2023-01-12-20-28-22-image.png)

- **의도적인** 빈 값을 의미

- ⭐️ 그러나 `null` 역시 **값**임. - *"비어있다"란 의미의 값*

- `object`(객체) 등이 들어있거나 반환되어야 하지만 없을 때 주로 사용
  
  - *"있어봐, 뭐 들어올 자리야"* / *"뭘 줘야 되는 거 아는데 줄 게 없어"*
  - 객체 생성이 실패한 경우 등에 대신 반환

- ⚠️ 주의! `typeof`가 `object`를 반환 *초기 오류* - 객체는 원시타입이 아님

```javascript
let x = null;
console.log(typeof null, typeof x); 
// object object
// object가 출력되는 것은 js의 설계 오류임.
// 객체와 null을 구분하지 못함 


// null 여부는 아래와 같이 확인한다. 
console.log(x === null);
// true
```


