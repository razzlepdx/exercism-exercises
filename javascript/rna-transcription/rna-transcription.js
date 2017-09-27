var DnaTranscriber = function(){};

var transcriptions = {
    "G":"C",
    "C":"G",
    "T":"A",
    "A":"U"
}

DnaTranscriber.prototype.toRna = function(dna) {
    var dnaArray = dna.split("");
    var rnaResult = [];
    dnaArray.forEach(function (nuc) {
        if (transcriptions.hasOwnProperty(nuc) == false) {
            throw Error("Invalid input");
        }
        
        rnaResult.push(transcriptions[nuc]);
    });
    return rnaResult.join('');
}

module.exports = DnaTranscriber;