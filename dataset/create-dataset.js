const rp = require('request-promise');
const fs = require('fs');
const saveJson = (filename, content) => {
    const filepath = './store/' + filename + '.json';
    fs.writeFileSync(filepath, content);
};
const getOpenbdDate = async (isbn) => {
    const options = {
        url: `http://api.openbd.jp/v1/get?isbn=${isbn}`,
        method: 'GET',
        timeout: 10 * 1000
    };
    await rp(options)
        .then((body) => {
        body = JSON.parse(body);
        if (body[0] == null) {
            console.log(`${isbn}: NULL`);
        }
        else {
            // 中身のあるJSONデータが返ってきたら、整形してファイル出力する
            console.log(`${isbn}: ${body[0]['summary']['title']}`);
            body = JSON.stringify(body, null, 2);
            saveJson(`${isbn}`, body);
        }
    })
        .catch((err) => {
        console.log(err);
    });
};
const isbn_start = 9784003200000;
const isbn_end = 9784003210000;
const batch_size = 100;
// isbn_startからisbn_endまでループを回して非同期処理getOpenbdDataメソッドを順に実行する
// そのときbatch_size分は並列処理され、全てのコールバックが返ってきたら次のバッチへ、というのをくり返す
(async () => {
    for (let num = isbn_start; num < isbn_end; num += batch_size) {
        // numからnum+batch_size-1までの分が並行処理される
        await Promise.all(Array.apply(null, new Array(batch_size)).map(async (v, i) => {
            await getOpenbdDate(num + i);
        }));
    }
    console.log('FINISHED');
})();
