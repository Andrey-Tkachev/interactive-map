import actions from '../constants/actionTypes';
import { languages } from '../executing';

export default (state = {
    activeLanguage: languages.JAVA_LANG,
    editors: [ {
                language: languages.JAVA_LANG,
                code: '',
                },
            ],
    input: '1 2 3\n',
}, action) => {
    switch (action.type) {
        case actions.CODE_CHANGE:
            return { ...state,
                    editors: state.editors.map(editor =>
                        (editor.language !== action.activeLanguage) ? editor : { ...editor,
                                                                                 code: action.code },
                    )};
        case actions.INPUT_CHANGE:
            return { ...state,
                    input: action.input };
        case actions.LANGUAGE_CHANGE:
            return { ...state,
                    activeLanguage: action.activeLanguage };
        default:
            return state;
    }
}
