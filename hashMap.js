export default class HashMap {
  constructor(capacity = 16, loadFactor = 0.75) {
    this.loadFactor = loadFactor;
    this.capacity = capacity;
    this.table = new Array(capacity);
    this.size = 0;
  }

  hash(key) {
    let hashCode = 0;

    const primerNumber = 31;
    for (let i = 0; i < key.length; i++) {
      hashCode = (primerNumber * hashCode + key.charCodeAt(i)) % this.capacity;
    }

    return hashCode;
  }

  resize() {
    const oldTable = this.table;
    this.capacity *= 2;
    this.table = new Array(this.capacity);
    this.size = 0;

    for (const bucket of oldTable) {
      if (bucket) {
        for (const [k, v] of bucket) {
          this.set(k, v);
        }
      }
    }
  }

  set(key, value) {
    const index = this.hash(key);
    if (!this.table[index]) {
      this.table[index] = [];
    }

    for (let pair of this.table[index]) {
      if (pair[0] === key) {
        pair[1] = value;
        return;
      }
    }

    this.table[index].push([key, value]);
    this.size++;
    if (this.size / this.capacity > this.loadFactor) {
      this.resize();
    }
  }

  get(key) {
    const index = this.hash(key);
    const bucket = this.table[index];
    if (bucket) {
      for (let [k, v] of bucket) {
        if (k === key) return v;
      }
    }
    return null;
  }

  has(key) {
    const index = this.hash(key);
    const bucket = this.table[index];
    if (bucket) {
      for (let [k, _] of bucket) {
        if (k === key) return true;
      }
    }
    return false;
  }

  remove(key) {
    const index = this.hash(key);
    const bucket = this.table[index];
    if (bucket) {
      for (let i = 0; i < bucket.length; i++) {
        const [k, _] = bucket[i];

        if (k === key) {
          bucket.splice(i, 1);
          this.size--;
          return true;
        }
      }
    }
    return false;
  }

  clear() {
    this.table = new Array(this.capacity);
    this.size = 0;
  }

  keys() {
    const result = [];
    for (const bucket of this.table) {
      if (bucket) {
        for (const [k, _] of bucket) {
          result.push(k);
        }
      }
    }
    return result;
  }

  values() {
    const result = [];
    for (const bucket of this.table) {
      if (bucket) {
        for (const [_, v] of bucket) {
          result.push(v);
        }
      }
    }
    return result;
  }

  entries() {
    const result = [];
    for (const bucket of this.table) {
      if (bucket) {
        for (const pair of bucket) {
          result.push(pair);
        }
      }
    }
    return result;
  }
}
